(function($){

	$.getArticles = function getArticles( options, fn ){
	//define our initial api url and data type we're expecting
	var ajaxOptions = {
		url: 'http://hearst.api.mashery.com/Article/search',
		jsonp: '_callback',
		dataType: 'jsonp',
		cache: true
	};
	
	//list of the valid api options
	var validArgs = [
		'article_category_id', 'article_id', 'article_section_id', 'article_source_id',
		'article_template_id', 'article_type_id', 'author_id', 'body', 'creation_date_begin',
		'creation_date_end', 'flow_id', 'import_ucid', 'is_an_import', 'issue_date',
		'keywords', 'last_updated_by', 'last_updated_date_begin', 'last_updated_date_end',
		'limit', 'print_issue_date', 'publish_date_begin', 'publish_date_end', 'published_only',
		'rights_for_syndicate_id', 'shape', 'site_id', 'sort', 'start', 'sub_heading', 'api_key',
		'ad_category_id', 'teaser', 'title', 'url_name', 'verbose', '_debug', '_pretty', '_callback'
	], validArgCount = 0; //keep track of valid options.. we're going to require at least 1
	
	//options that require an ISO 8601 formatted date string
	var dateArgs = [
		'creation_date_begin', 'creation_date_end',
		'publish_date_begin', 'publish_date_end',
		'last_updated_date_begin', 'last_updated_date_end'
	], date; //temp date we'll use for conversions
	
	//loop through all of the options being passed in
	for ( var prop in options ){
		if ( options.hasOwnProperty(prop) ){
			//check to see if the option is valid
			if ( validArgs.indexOf( prop ) > -1 ){
				validArgCount++; //increment the number of valid args we have
			} else {
				//if the arg passed isn't valid, shoot out a warning and remove it
				console.warn('getArticles: ' + prop + ' is not a valid option.');
				delete options[ prop ];
			}
			//check to see if this argument is a date
			if ( dateArgs.indexOf( prop ) > -1 ){
				//try to create a new Date object from the value
				date = new Date( options[prop] );
				//if the product is an invlid date, throw an error
				if ( date.toString() === "Invalid Date" || options[prop] === false || options[prop] === true || options[prop] === null ){
					throw new Error('getArticles: ' + prop + ' contains an invalid date.');
				}
				//assure the arg is set to a ISO formatted date string
				options[ prop ] = date.toISOString();
			}
		}
	}
	//if we don't have at least one valid arg, throw an error
	if ( validArgCount < 1 ){ throw new Error('getArticles: Invalid Options'); }
	//add the arguments and the callback to the ajax options
	$.extend( ajaxOptions, {
		data:    options,
		success: ( $.isFunction(fn) ) ? fn : $.noop
	});
	//execute the ajax request and return the promise returned by jquery
	return $.ajax( ajaxOptions );
};
})( jQuery );