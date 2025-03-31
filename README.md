# Real Estate Data Engineering Project

![Pipeline](https://github.com/user-attachments/assets/773d8646-dcd9-4072-bbd7-32927aa71c0e)

![image](https://github.com/user-attachments/assets/9e606154-b097-432d-b932-3379c58e50ce)

![image](https://github.com/user-attachments/assets/dbb05f30-36b2-4410-ae60-2467d0697fbf)

![image](https://github.com/user-attachments/assets/47e48bd4-c62d-4979-8c34-01696da66ad6)





## Overview
This project is a **data engineering pipeline** that extracts, processes, and stores real estate listings from property-selling websites like **Property Finder** and **Bayut**. The goal is to **scrape, clean, and store real estate data** into a **PostgreSQL database**, utilizing **Apache Spark** for data processing.

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

## How It Works

### **1️⃣ Web Scraping (`scrapper.py`)**  
- Scrapes real estate listings from **Property Finder** and **Bayut**.  
- Extracts data like **title, price, location, size, bedrooms, bathrooms, and URL**.  
- Saves raw data in the `/data` folder with patterns data/bayut_{date}.csv and property_finder_{date}.csv.  

### **2️⃣ Data Processing (`preprocessing.py`)**  
- It Processes the latest downloaded scraped data for the day.
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

## Ideas if someone wants to add on this project or what i plan to do later:
- [ ] Automate daily data scraping (Airflow)
- [ ] Add machine learning model for price prediction 

