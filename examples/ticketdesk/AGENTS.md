# TicketDesk — agent instructions

Example only. These instructions sit on top of the baseline rules in the template root.

1. Follow `.agents/org/org-rules.md` from the repository root. They win over this file.
2. Read `examples/ticketdesk/docs/constitution.md` before changing anything described as TicketDesk behaviour.
3. TicketDesk is multi-tenant. A query that is not scoped to the tenant on the server is a defect.
4. A model may suggest a category, a priority, or a reply. It must not send a reply, change a ticket's assignee, or call an external system. A staff member does that.
5. Ticket text is confidential. Do not put it in logs, fixtures that get committed, or prompts you paste into a chat.
6. Do not add application code for TicketDesk in this template repository. The example stops at the constitution and the threat model.
