from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class MessageRequest(BaseModel):
    query: str = Field(..., description="Plain text user message or button payload identifier")
    app_id: Optional[str] = Field("7777", description="App application identifier")
    sessionid: str = Field(..., description="Unique chat session identifier")
    clientId: Optional[int] = Field(208, description="Client account identifier")
    botId: Optional[int] = Field(7777, description="Chat bot identifier")
    extraParms: Optional[str] = Field(None, description="Serialized JSON or string of extra parameters")

class ChatBotResponse(BaseModel):
    type: str = Field("adaptiveCard", description="Type of container structure")
    responseType: str = Field("", description="State category of active response")
    body: List[Dict[str, Any]] = Field([], description="Visual building blocks")
    actions: List[Dict[str, Any]] = Field([], description="Interactive actions array")
    buttons: Optional[List[Dict[str, Any]]] = Field([], description="Flat list of buttons")

class TicketCreateSchema(BaseModel):
    user_id: str
    customer_name: str
    mobile_number: str
    issue_type: str
    category: str
    sub_category: str
    description: Optional[str] = ""

class TicketResponseSchema(BaseModel):
    ticket_id: str
    user_id: str
    customer_name: str
    mobile_number: str
    issue_type: str
    category: str
    sub_category: str
    description: Optional[str]
    status: str
    assigned_to: str
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True
