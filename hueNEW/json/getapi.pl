# -*- compile-command: "perl getapi.pl" -*-

for ($y=2000; $y<=2013; $y++) { 
    for $m (10, 2, 5, 8) {
        $month = sprintf("%02d", $m);
        $file = "runway$month$y.json";

        $a = "wget -O $file 'http://hearst.api.mashery.com/Article/search?_pretty=1&total=1&limit=200&_json={%22article_section_id%22:[11561,11562,11563,11564,11565]}&pages=full&&api_key=c9pj47r6q7p7b3gugn5ddb8c&creation_date_begin=$y-$month-01T12:00:00.000Z&creation_date_end=$y-$month-30T12:00:00.000Z'";

        print "$a\n";
        system $a;

    }
}

