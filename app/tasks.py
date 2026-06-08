import logging
import time
from celery import shared_task
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

logger = logging.getLogger(__name__)

# Sync connection helper for Celery workers
try:
    sync_engine = create_engine(
        settings.DATABASE_SYNC_URL,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10
    )
    SyncSessionLocal = sessionmaker(bind=sync_engine)
except Exception as e:
    logger.error(f"Failed to create sync database engine: {e}")
    SyncSessionLocal = None

@shared_task(bind=True, max_retries=3, default_retry_delay=10)
def process_crm_ticket(self, ticket_data: dict):
    """
    Background Celery task that processes and persists a newly created CRM ticket.
    Simulates sending alerts and syncing with core CRM banking databases.
    """
    from app.models import Ticket  # Import inside to prevent circular import loops

    logger.info(f"Processing CRM Ticket: {ticket_data.get('ticket_id')}")
    
    # Simulate API latency connecting to core CRM / ticketing endpoint
    time.sleep(2.0)
    
    if not SyncSessionLocal:
        logger.error("Database connection session is not available.")
        return {"status": "FAILED", "reason": "No database session available"}

    session = SyncSessionLocal()
    try:
        ticket_id = ticket_data["ticket_id"]
        # Save ticket into MySQL database
        existing_ticket = session.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()
        if not existing_ticket:
            ticket = Ticket(
                ticket_id=ticket_id,
                user_id=ticket_data["user_id"],
                customer_name=ticket_data["customer_name"],
                mobile_number=ticket_data["mobile_number"],
                issue_type=ticket_data["issue_type"],
                category=ticket_data["category"],
                sub_category=ticket_data["sub_category"],
                description=ticket_data.get("description", ""),
                status="OPEN",
                assigned_to="Support Team"
            )
            session.add(ticket)
            session.commit()
            logger.info(f"Ticket {ticket_id} successfully persisted in MySQL.")
        else:
            logger.warning(f"Ticket {ticket_id} already exists.")
            
        # Simulating external webhook trigger / SMS alert dispatch
        logger.info(f"Notified Support Team of new ticket {ticket_id}")
        return {"status": "SUCCESS", "ticket_id": ticket_id}
        
    except Exception as exc:
        session.rollback()
        logger.error(f"Error saving ticket to database, retrying: {exc}")
        raise self.retry(exc=exc)
    finally:
        session.close()
