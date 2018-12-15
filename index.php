<?php 

require('simple_html_dom.php');
echo "ini web scrapp ";
 
// Website link to scrap
$website = 'https://www.bukalapak.com/products?from=omnisearch&search%5Bkeywords%5D=mod%20vapor&search_source=omnisearch_category&source=navbar';
 
 
// Create DOM from URL or file
$html = file_get_html($website);
 
// Print webpage content  
echo $html;
?>