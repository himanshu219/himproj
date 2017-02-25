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
      nohup python manage.py runserver 56894 &

**APIENDPOINTS**

curl http://localhost:8000/api/companyinfo/L01132WB1918PLC003029/
OUTPUT:
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
      
http://localhost:8000/api/directorinfo/00005684/

      
**Things Learned**
    Serializing many to many field      
      
**Future Tasks **
    Bulk Insertion of Data    
    API Test Cases
    Query Optimization

  ```