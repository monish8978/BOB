// State configuration for simulator client
const MOCK_USER_ID = "BOB-USER-99";
const chatMessages = document.getElementById("chat-messages");
const chatInput = document.getElementById("chat-input");
const quickRepliesContainer = document.getElementById("quick-replies");
const ticketList = document.getElementById("ticket-list");

// Document ready entry
document.addEventListener("DOMContentLoaded", () => {
    // Perform initial loading
    initializeChat();
    loadCRMTickets();
    
    // Poll for new CRM tickets every 5 seconds to show active background celery updates
    setInterval(loadCRMTickets, 5000);
});

// Initialize chatbot by requesting initial greeting
async function initializeChat() {
    chatMessages.innerHTML = "";
    quickRepliesContainer.innerHTML = "";
    
    // Check if there are existing logs, or trigger standard welcome message
    try {
        const response = await fetch(`/api/logs/${MOCK_USER_ID}`);
        const logs = await response.json();
        
        if (logs && logs.length > 0) {
            logs.forEach(log => {
                appendBubble(log.sender.toLowerCase(), log.message_text, false);
            });
            scrollToBottom();
        } else {
            // Trigger main menu initial greetings
            submitMessage("", "MAIN_MENU");
        }
    } catch (e) {
        console.error("Failed to load logs:", e);
        submitMessage("", "MAIN_MENU");
    }
}

// Send user text from input bar
function sendMessage() {
    const text = chatInput.value.trim();
    if (!text) return;
    
    appendBubble("user", text);
    chatInput.value = "";
    quickRepliesContainer.innerHTML = "";
    
    submitMessage(text, null);
}

// Handle enter key submit
function handleEnterKey(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

// Action button / postback button press handler
function handleActionButton(title, payload) {
    appendBubble("user", title);
    quickRepliesContainer.innerHTML = "";
    
    submitMessage(title, payload);
}

// Quick reply pill click handler
function handleQuickReply(title, payload) {
    appendBubble("user", title);
    quickRepliesContainer.innerHTML = "";
    
    submitMessage(title, payload);
}

// Send payload to backend
async function submitMessage(message, payload) {
    // Add custom typing indicator bubble
    const typingIndicator = appendTypingIndicator();
    
    try {
        const response = await fetch("/api/simulate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                query: payload || message || "",
                app_id: "7777",
                sessionid: MOCK_USER_ID,
                clientId: 208,
                botId: 7777,
                extraParms: JSON.stringify({ source: "webchat", csid: "731779738973688" })
            })
        });
        
        const data = await response.json();
        
        // Remove typing indicator bubble
        typingIndicator.remove();
        
        // Render bot message
        appendBotResponse(data);
        
    } catch (e) {
        typingIndicator.remove();
        appendBubble("bot", "⚠️ Network connection lost. Please check if backend services are active.");
        console.error("Simulation error:", e);
    }
}

// Appends standard text bubble
function appendBubble(sender, text, animate = true) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", sender);
    if (!animate) messageDiv.style.animation = "none";
    
    messageDiv.innerHTML = formatMarkdown(text);
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
    return messageDiv;
}

// Appends typing loader animation
function appendTypingIndicator() {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", "bot");
    messageDiv.innerHTML = `
        <div style="display: flex; gap: 4px; align-items: center; padding: 4px 8px;">
            <i class="fa-solid fa-circle" style="font-size: 6px; animation: bounce 1.2s infinite; color: var(--text-secondary);"></i>
            <i class="fa-solid fa-circle" style="font-size: 6px; animation: bounce 1.2s infinite 0.2s; color: var(--text-secondary);"></i>
            <i class="fa-solid fa-circle" style="font-size: 6px; animation: bounce 1.2s infinite 0.4s; color: var(--text-secondary);"></i>
        </div>
        <style>
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-4px); }
            }
        </style>
    `;
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
    return messageDiv;
}

// Appends multi-featured bot response structure (AdaptiveCard layout)
function appendBotResponse(data) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", "bot");
    
    let botText = "";
    let choices = [];
    
    // Parse AdaptiveCard body
    if (data.body && data.body.length > 0) {
        data.body.forEach(block => {
            if (block.type === "TextBlock") {
                botText = block.text;
            } else if (block.type === "Button" && block.choices) {
                choices = block.choices;
            }
        });
    }
    
    // 1. Set text content with custom formatting
    let contentHtml = formatMarkdown(botText || data.text || "");
    
    // 2. Render choice buttons inside the message bubble
    if (choices && choices.length > 0) {
        contentHtml += `<div class="bot-action-buttons">`;
        choices.forEach(choice => {
            contentHtml += `
                <div class="action-btn" onclick="handleActionButton('${choice.title}', '${choice.id}')">
                    ${choice.title}
                </div>
            `;
        });
        contentHtml += `</div>`;
    }
    
    messageDiv.innerHTML = contentHtml;
    chatMessages.appendChild(messageDiv);
    
    // Clear quick replies since they are merged into body choices
    quickRepliesContainer.innerHTML = "";
    
    scrollToBottom();
}

// Utility formatting helper
function formatMarkdown(text) {
    if (!text) return "";
    
    let html = text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
        
    // Bold formats
    html = html.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
    html = html.replace(/\*(.*?)\*/g, "<strong>$1</strong>");
    
    // Newlines conversion
    html = html.replace(/\n/g, "<br>");
    
    // Bullet formats
    html = html.replace(/•\s(.*?)(<br>|$)/g, "<li>$1</li>");
    html = html.replace(/-\s(.*?)(<br>|$)/g, "<li>$1</li>");
    
    return html;
}

function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Fetch all tickets logged in CRM board
async function loadCRMTickets() {
    try {
        const response = await fetch("/api/tickets");
        const tickets = await response.json();
        
        // Update dashboard summaries
        document.getElementById("total-tickets").innerText = tickets.length;
        document.getElementById("open-tickets").innerText = tickets.filter(t => t.status === "OPEN").length;
        
        if (tickets.length === 0) {
            ticketList.innerHTML = `
                <div class="empty-state">
                    <i class="fa-solid fa-envelope-open-text empty-icon"></i>
                    <h3>No Tickets Created Yet</h3>
                    <p>Simulate the chatbot, choose <strong>"No"</strong> to help queries, or type <strong>"ticket"</strong> to create a support ticket using background Celery workers.</p>
                </div>
            `;
            return;
        }
        
        // Populate tickets list
        ticketList.innerHTML = "";
        tickets.forEach(ticket => {
            const ticketDate = new Date(ticket.created_at).toLocaleString();
            
            const ticketDiv = document.createElement("div");
            ticketDiv.classList.add("ticket-item");
            
            ticketDiv.innerHTML = `
                <div class="ticket-item-header">
                    <div class="ticket-id-section">
                        <h3>${ticket.ticket_id}</h3>
                        <p><i class="fa-regular fa-clock"></i> ${ticketDate}</p>
                    </div>
                    <div class="ticket-tags">
                        <span class="ticket-tag tag-issue">${ticket.issue_type}</span>
                        <span class="ticket-tag tag-status">${ticket.status}</span>
                    </div>
                </div>
                
                <div class="ticket-details-grid">
                    <div><span class="detail-lbl">Name:</span> <span class="detail-val">${ticket.customer_name}</span></div>
                    <div><span class="detail-lbl">Mobile:</span> <span class="detail-val">${ticket.mobile_number}</span></div>
                    <div><span class="detail-lbl">Category:</span> <span class="detail-val">${ticket.category}</span></div>
                    <div><span class="detail-lbl">Sub-Cat:</span> <span class="detail-val">${ticket.sub_category}</span></div>
                </div>
                
                <div class="ticket-desc">
                    <strong>Description:</strong> ${ticket.description || "No description provided."}
                </div>
            `;
            
            ticketList.appendChild(ticketDiv);
        });
    } catch (e) {
        console.error("Failed to load tickets:", e);
    }
}

// Reset session variables
async function resetDeveloperSession() {
    try {
        const response = await fetch(`/api/reset/${MOCK_USER_ID}`, { method: "POST" });
        const result = await response.json();
        
        // Re-initialize chat greeting and refresh logs view
        initializeChat();
        loadCRMTickets();
        
        // Show status feedback
        console.info(result.message);
    } catch (e) {
        console.error("Failed to reset session:", e);
    }
}
