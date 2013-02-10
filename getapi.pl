# -*- compile-command: "perl getapi.pl" -*-


$y = 2012;

#$m = 11;
#for ($m=1; $m<=12; $m++)
#for ($y=2000; $y>=1990; $y--) { 

for $m (3)
{
$month = sprintf("%02d", $m);
$file = "runway$y$month.json";
$day = 30;
$day = 28 if $m == 2;

$a = "wget -O $file 'http://hearst.api.mashery.com/Article/search?limit=200&total=1&start=0&api_key=c9pj47r6q7p7b3gugn5ddb8c&creation_date_begin=$y-$month-01T12:00:00.000Z&creation_date_end=$y-$month-${day}T12:00:00.000Z'";

#$a = "wget -O $file 'http://hearst.api.mashery.com/Article/search?_pretty=1&start=0&total=1&limit=200&_json={%22article_section_id%22:[11561,11562,11563,11564,11565]}&pages=full&&api_key=c9pj47r6q7p7b3gugn5ddb8c&creation_date_begin=$y-$month-01T12:00:00.000Z&creation_date_end=$y-$month-${day}T12:00:00.000Z'";



        print "$a\n";
        system $a;

sleep 5;
}






#http://hearst.api.mashery.com/Article/search?_version=2&total=1&start=0&limit=10&publish_date_begin=1900-01-01T05:00:00.000Z&publish_date_end=2007-12-31T05:00:00.000Z
