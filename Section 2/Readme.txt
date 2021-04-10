
The attached docker file will pull the postgres latest version from hub and execute the attached init.sql commands to create the required objects in the base version

Issue below command to pick the docker to use the docker file and create the required image . Please issue the below command from the path where we have Dockerfile and init.sql
docker build -t postgres-section3 . 

To start the new docker container instance use below command 
docker start postgres-section3


Please use below query to the details. 

1) 
select cs.salesdate,cs.salestime,c.clientname,c.clientphone,cd.carmodelname,s.salespersonname,cs.carserialno,m.manufacutername from carsales cs inner join client c on cs.clientid=c.clientid inner join salesperson s on cs.salespersonid=s.salespersonid inner join cardetails cd on cd.carmodelid=cs.carmodelid inner join manufacturer m on cd.manufacturerid = m.manufacturerid order by cs.salesdate,cs.salestime

2) select sales_month,manufacutername,salesvolume from (select extract(month from cs.salesdate) sales_month,m.manufacutername,count(*) salesvolume from carsales cs inner join cardetails cd on cs.carmodelid=cs.carmodelid inner join manufacturer m on m.manufacturerid=cd.manufacturer where extract (month FROM salesdate) = extract (month FROM CURRENT_DATE) group by extract(month from cs.salesdate) sales_month,m.manufacutername) order by salesvolume desc limit 3;

We can use analytic function also to fetch top 3 manufacturer by sales volume , skippin it due to time constraint

