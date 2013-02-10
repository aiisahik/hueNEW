hueKnewApp = new Backbone.Marionette.Application();

	// set initial time and progress
	window.initialTime = +new Date;
	window.progress = 0;

	hueKnewApp.addRegions({
	  mainRegion: "#hueKnewApp_gallery"
	  // fieldRegion: "#hueKnewApp_fields"
	});

	ImageObject = Backbone.Model.extend({
	});

	ImageObjects = Backbone.Collection.extend({
		model: ImageObject
	});

	ImageItemView = Backbone.Marionette.ItemView.extend({
		tagName: "div",
		className: "",
		template: "#imageitem-template",
		events: {
		},
		initialize: function () {
			// console.log(this.model.toJSON());
		},
		onRender: function(){
			console.log(this.$el);
		}
	});

	ImageCollectionView = Backbone.Marionette.CollectionView.extend({
		tagName: "div",
		className: "collection",
		template: "#collectionview-template",
		itemView: ImageItemView,
		// template: "#formfields-template",
		onRender: function(){
			console.log(this.$el);
			$()
		},
		appendHtml: function(collectionView, itemView, index){
    		collectionView.$el.append(itemView.el);
  		}

		// appendHtml: function(collectionView, itemView){
		// 	itemView.parentView = this;
		// 	// collectionView.$("#npcShelfFormApp_fields").append(itemView.el);
		// 	// provide a way for the itemView to access the parent CompositeView
			
		// }
	});

	hueKnewApp.addInitializer(function(options){
		
		imageCollectionView = new ImageCollectionView({
			collection: window.imageObjects,
			itemView: ImageItemView
		});
		
		hueKnewApp.mainRegion.show(imageCollectionView);
	});

	hueKnewApp.addInitializer(function(options){
  		// new hueKnewAppRouter();
  		Backbone.history.start();
	});

