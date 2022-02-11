# ICP-3

#### Complete the following:

```
Name: Javkhlan Enkhjin
Email: jenmh@umkc.edu
ICP-Link: https://github.com/UMKC-APL-PythonDeepLearing/icp_3-JavkhlanEnkhjin.git
Video: https://youtu.be/FS9HPBRjiAw
```
---
```
Partner Name: Mohamad Abboud
Partner Email: maadz9@umkc.edu
Partner ICP-Link: https://github.com/UMKC-APL-PythonDeepLearing/icp_3-MoAbboud
```
<br/>
 
Write brief explanation here:

1.

We created the class employee with its class attribute (count_emp) which will be used to store the number of employees, constructer, then we created the full time and part time employee class that contained the GiveRaise method that takes in the default values for 10% and 5% respectively.

In the employee class we added the pay, fire, isEmployed functions. From there we are ready to create the start function that will read from the input file according to the keywords that were presented in the input file for NEW, RASIE, PAY, and Fire. A function was also created to calculate the average salary of both the Full Time and Part Time employees. Finally an output file is created matching the criteria found in the ICP

1.2.

A car class was created that contais a constructer with private variables initialized for year, make, and model. After that we created a private function using __printinfo

We then created a public method that references the private method. Finally we created an object of the car class Toyota. Which was then used to call the printinfo method using Toyota.printinfo().

2.

Using BeautifulSoup we were able to webscrap the wikipedia page (Machine Learning) for all its images. After using the BeautifulSoup function, we printed the page title using obj.title.string. After that we searched through the page for all the anchor elements using obj.find_all('a', {'class': 'image'}) which only looks for the anchor elements that use the class image. Then we iterate over each of the anchor tags, looking for the img tags, next we get the src tags inside the img tag using link.get('src'). Once done we print the src for each of the image.
