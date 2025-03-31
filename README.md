# Real Estate Data Engineering Project

## Overview
This project is a **data engineering pipeline** that extracts, processes, and stores real estate listings from property-selling websites like **Property Finder** and **Bayut**. The goal is to **scrape, clean, and store real estate data** into a **PostgreSQL database**, utilizing **Apache Spark** for scalable data processing.

## Tech Stack
- **Python** → Web Scraping & Data Processing  
- **Apache Spark** → Distributed Data Processing  
- **PostgreSQL** → Data Storage  
- **Docker & Docker Compose** → Containerization  

---

## Project Structure
```
real-estate-data-engineering
├── data                 
├── Dockerfile             
├── docker-compose    
├── scrapper.py           
├── preprocessing.py        
├── load_data.py            
├── main.py                 
├── requirements.txt        
└── README.md                 
```

---

## 🛠How It Works

### **1️⃣ Web Scraping (`scrapper.py`)**  
- Scrapes real estate listings from **Property Finder** and **Bayut**.  
- Extracts data like **title, price, location, size, bedrooms, bathrooms, and URL**.  
- Saves raw data in the `/data` folder.  

### **2️⃣ Data Processing (`preprocessing.py`)**  
- Uses **Apache Spark** to clean and transform the scraped data.  
- Handles **missing values, duplicates, and data formatting**.
- Applying some logic such as extracting the sub-location from location. 

### **3️⃣ Loading Data (`load_data.py`)**  
- Connects to **PostgreSQL** and creates a table.  
- Loads the cleaned data into the database.  

### **4️⃣ Running the Pipeline (`main.py`)**  
- Runs all scripts **in sequence** to complete the pipeline.  

---

```

## Future Improvements
- [ ] Automate daily data scraping
- [ ] Add machine learning model for price prediction  

