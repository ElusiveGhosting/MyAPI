# MyAPI using Chalice

1. Configure AWS credentials : ( Needed to deploy the API => API Gateway + Lambda )
   
		   $ mkdir ~/.aws
		   $ cat >> ~/.aws/config
			 [default]
			 aws_access_key_id=YOUR_ACCESS_KEY_HERE
			 aws_secret_access_key=YOUR_SECRET_ACCESS_KEY

2. Clone the repository
   
           $ git clone https://github.com/ElusiveGhosting/MyAPI.git
 
3. Change in the code directory
   
           $ cd MYAPI
   
4. Deployment

   local :
      
	      $ chalice local
	
	Cloud/AWS Account :
	      
		  $ chalice deploy
		  

5. Testing Deployment (When deployed to cloud change API gateway hostname provided in bash after deployment)
   
   Postman :
         
          https://www.softwaretestinghelp.com/how-to-use-postman/		 
			
   Curl :
         
		  $ curl -i http://localhost:4001/  
		    {'hello': 'world'}
	    

		  
6. Delete deployment from AWS( stop charges to Credit card )

          $ chalice delete

