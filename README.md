**Building Project**
  ```
    pip install -r requirements.txt
    
    python manage.py syncdb
    
    python manage.py migrate
    
    for inserting data from csv 
    change file_name variable in migratedata.py
    and run python manage.py migratedata
  ```
  
**Running Server Locally**
  ```
      nohup python manage.py runserver 0.0.0.0:56894 &
  ```
    
**API ENDPOINTS**

1.[COMPANY API] (http://localhost:56894/companyinfo/L01132WB1918PLC003029/)
  METHOD=GET
  
    {
        cin: "L01132WB1918PLC003029",
        company_name: "NAGA DHUNSERI GROUP LTD.",
        status: "ACTIVE",
        address1: "DHUNSERI HOUSE",
        address2: "4A, WOODBURN PARK",
        full_address: null,
        city: "KOLKATA",
        pincode: 700020,
        type: "PUBLIC",
        authorised_capital: "25000000.00",
        paidup_capital: "10000000.00",
        incorporation_date: "1918-08-26",
        agm_date: "2015-09-21",
        balancesheet_date: "2015-03-31",
        directors: [
            {
                designation: "DIRECTOR",
                appointment_date: "1974-08-31",
                director_din: "00005684",
                director_name: "CHANDRA KUMAR DHANUKA"
            },
            {
                designation: "DIRECTOR",
                appointment_date: "1977-05-23",
                director_din: "00012320",
                director_name: "INDRA KISHORE KEJRIWAL"
            },
            {
                designation: "DIRECTOR",
                appointment_date: "2003-01-31",
                director_din: "00005666",
                director_name: "MRIGANK DHANUKA"
            },
            {
                designation: "MANAGING DIRECTOR",
                appointment_date: "2005-10-31",
                director_din: "00005677",
                director_name: "ARUNA DHANUKA"
            },
            {
                designation: "DIRECTOR",
                appointment_date: "2006-01-31",
                director_din: "00122221",
                director_name: "RAJEEV RUNGTA"
            },
            {
                designation: "DIRECTOR",
                appointment_date: "2009-01-28",
                director_din: "00133700",
                director_name: "GOBIND RAM GOENKA"
            },
            {
                designation: "CFO",
                appointment_date: "2014-08-13",
                director_din: "ACZPB2533Q",
                director_name: "HARI PRASAD BHUWANIA"
            },
            {
                designation: "SECRETARY",
                appointment_date: "2014-11-01",
                director_din: "ALDPS1750R",
                director_name: "ASHIT KUMAR SARKAR"
            }
        ],
        category: "Company limited by shares",
        state: "KOLKATA",
        subcategory: "Indian Non-Government Company",
        country: "INDIA"
    }
        
2.[DIRECTOR API] (http://localhost:56894/api/directorinfo/00005684/)
   METHOD=GET

    {
        din: "00005684",
        name: "CHANDRA KUMAR DHANUKA",
        companies: [
            {
                appointment_date: "1974-08-31",
                company_cin: "L01132WB1918PLC003029",
                company_company_name: "NAGA DHUNSERI GROUP LTD."
            }
        ]
    }


**API Design**
   API fields can be changed using fields variable

**Schema Design**
     ![alt text](http://i67.tinypic.com/2epm238.png)
    
**DATA Insertion Script**

   Script is written in such a way that it avoids duplicate entry by using get_or_create function
   Also you can tweak script for any other file or data format using these settings
   FILE_NAME = file path
   COL_NO = number of columns that contain company's information
   DIR_FIELDS_LENGTH = number of columns that contain director's information
    


**Things Learned**
    
   1. Normalizing & Reading file with multiple columns of same name by keeping track of number of columns
        Ex Since all directors' columns are in one row so need to split them up while creating entry in director table
   2. To access django dev server need to run it in 0.0.0.0:56894    
   3. Things I knew but I forgot
        - Serializing M2M fields
        - django saves data in unicode so str is not allowed as it has ascii encoding by default
        - creating virtualenv with system packages virtualenv --system-site-packages
                     
**Future Tasks**
   1. Bulk Insertion of Data 
   2. API Test Cases
   3. Query Optimization
