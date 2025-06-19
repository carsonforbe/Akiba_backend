# 💼 ChamaLink - Backend API

**ChamaLink** is a backend REST API built with Django and Django REST Framework, designed to digitize and streamline the management of *chamas* (informal savings/investment groups) in Kenya.

## 🚀 Features

- 🧑‍🤝‍🧑 **User Management** – Signup, login, and role-based access (admin, treasurer, member)
- 🏘 **Group Management** – Create and manage chamas, invite and remove members
- 💰 **Transactions** – Record contributions, withdrawals, and view ledger
- 📊 **Reports** – Generate group financial summaries
- 📩 **Notifications** – Send SMS or push alerts for transactions and updates

---

## 📁 Project Structure

backend-api/
├── chamalink/ # Django project settings
├── apps/
│ ├── users/ # User auth, roles
│ ├── groups/ # Chama creation and member management
│ ├── transactions/ # Contribution tracking and ledgers
│ ├── reports/ # Financial reporting
│ └── notifications/ # SMS and push notifications
├── tests/ # Unit and integration tests
├── Dockerfile # Docker container definition
├── requirements.txt # Python dependencies
