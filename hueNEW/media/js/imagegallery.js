

	ImageObject = Backbone.Model.extend({
	});

	ImageObjects = Backbone.Collection.extend({
		model: ImageObject
	});

	ImageItemView = Backbone.Marionette.ItemView.extend({
		tagName: "div",
		className: "image",
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

