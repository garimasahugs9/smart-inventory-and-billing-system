# 🏪 Smart Inventory and Billing System

A Streamlit web app for managing a small business's customers, products, and sales, with built-in analytics reports to understand how the business is performing.

## 📸 Screenshots

### Dashboard
<img width="1920" height="980" alt="dashboard_1" src="https://github.com/user-attachments/assets/ee8b9edc-c7de-4a58-9b6e-465e46f422d7" />




### Customer Management
<img width="1920" height="980" alt="customers" src="https://github.com/user-attachments/assets/51f1dc6f-33f1-4e15-8611-9700886fbfe1" />


### Product Management
<img width="1920" height="980" alt="products_1" src="https://github.com/user-attachments/assets/947085f9-ceb1-4ffe-8d65-e272f977bd8d" />


### Sales Management
<img width="1920" height="980" alt="sales" src="https://github.com/user-attachments/assets/3d17968b-ec7f-4f6c-9d85-a157f26dc73a" />


### Analytics & Reports
| Sales Summary | Daily Sales Trend |
|---|---|
| ![Sales Summary](screenshots/analytics-summary.png) | ![Daily Sales Trend](screenshots/analytics-trend.png) |

| Top Selling Products | Customer Purchase History |
|---|---|
| ![Top Selling Products](screenshots/top-products.png) | ![Customer Purchase History](screenshots/customer-history.png) |

## ✨ Features

**Dashboard**
- Overview of total customers, products, and sales

**Customer Management**
- View, add, update, and delete customers

**Product Management**
- View, add, update, and delete products (name, description, price, quantity)

**Sales Management**
- Create new sales for a selected customer
- View all sales
- Generate bills

**Analytics & Reports**
- Sales summary (total sales, total revenue) with a daily sales trend line chart
- Sales by date range
- Top selling products (table and bar chart)
- Low stock alerts
- Customer purchase history

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Streamlit
- **Database:** SQL ([DATABASE NAME, e.g. MySQL / SQLite])
- **Libraries:** [e.g. pandas, mysql-connector-python]

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- [DATABASE NAME] installed and running

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/[your-username]/[repo-name].git
   cd [repo-name]
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database
   ```bash
   # [Add your steps here, e.g. run schema.sql and the data insert script]
   ```

4. Run the app
   ```bash
   streamlit run [app.py]
   ```

The app opens at `http://localhost:8501`.

## 📁 Project Structure

```
[repo-name]/
├── [app.py]
├── [database / SQL files]
├── requirements.txt
├── screenshots/
└── README.md
```

## 📝 Note

The data shown in the screenshots is sample data used for demonstration.

## 🔮 Future Improvements

- User login and role-based access
- Export bills as PDF
- Deploy the app online

## 👤 Author

**[Your Name]**
[GitHub](https://github.com/[username]) | [LinkedIn](https://linkedin.com/in/[username])
