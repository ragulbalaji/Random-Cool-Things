<?php
/*
* Author: Ragul Balaji
* Date: 13 July 2015
* Desc: Needs PHP5, Internet, grep, cut & OSX say
*/


echo "\nRecieve Wisdom -- (C) Ragul Balaji 2015\n";
echo "Wisdom thanks to WisdomofDeepakChopra.com\n";
echo "Automation & Speech Syn. by Ragul Balaji\n";

echo "\n\nHow Much Wisdom Do You Want: ";

$i = intval(fgets(STDIN));

while($i){
	echo "\n".$i;
	exec('curl http://www.wisdomofchopra.com/iframe.php --silent | grep "&quot;" | cut -d\; -f2 | cut -d\& -f1 | say');
	$i--;
}

?>
