$(document).ready(function() {
    var form_order = $('#product-stuff-cont');
    var form_liked = $('#product-liked-form');

    function update_order(product_id, count, is_delete, loc) {
        var data = {};
        data.product_id = product_id;
        data.count = count;
        if (loc === 'product') {
            var csrf_token = $('#product-stuff-cont [name="csrfmiddlewaretoken"]').val();
            var url = form_order.attr("action");
        }
        if (loc === 'main') {
            var csrf_token = $('.product-stuff-cont [name="csrfmiddlewaretoken"]').val();
            var url = '/update_order';
            if (is_delete) {
                $('.' + product_id + '-to-remove-order-class').remove()
            }
        }
        data['is_delete'] = is_delete;
        data["csrfmiddlewaretoken"] = csrf_token;
        $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 console.log("OK");
             },
             error: function(){
                 console.log("error")
             }
         })
    }

    form_order.on('submit', function(event){
        event.preventDefault();
        var count = $('#product-to-order-count').val();
        var submit_btn = $('#product-to-order-butt');
        var product_id =  submit_btn.data("product_id");
        var is_delete = submit_btn.data("is_delete");
        var loc = submit_btn.data("loc");
        update_order(product_id, count, is_delete, loc);
    });

    function update_favorites(product_id, is_delete, loc) {
        var data = {};
        data.product_id = product_id;
        if (loc === 'product') {
            var csrf_token = $('#product-liked-form [name="csrfmiddlewaretoken"]').val();
            var url = form_liked.attr("action");
        }
        if (loc === 'main') {
            var csrf_token = $('.product-liked-form [name="csrfmiddlewaretoken"]').val();
            var url = '/update_favorites';
            if (is_delete) {
                $('.' + product_id + '-to-remove-fav-class').remove()
            }
        }
        data["csrfmiddlewaretoken"] = csrf_token;
        data['is_delete'] = is_delete;
        console.log(data);
        $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 console.log("OK");
             },
             error: function(){
                 console.log("error")
             }
         })
    }

    form_liked.on('submit', function(event) {
        event.preventDefault();
        var submit_btn = $('#like-butt');
        var product_id =  submit_btn.data("product_id");
        var is_delete = submit_btn.data("is_delete");
        var loc = submit_btn.data("loc");
        update_favorites(product_id, is_delete, loc);
    });

    $(document).on('click', '.like-butt', function(event){
         event.preventDefault();
         var product_id = $(this).data("product_id");
         var is_delete = $(this).data("is_delete");
         var loc = $(this).data("loc");
         update_favorites(product_id, is_delete, loc);
     });

    $(document).on('click', '.to-order-butt', function(event){
        event.preventDefault();
        var product_id = $(this).data("product_id");
        var count = $('.'+product_id+'-product-input').val();
        var is_delete = $(this).data("is_delete");
        var loc = $(this).data("loc");
        update_order(product_id, count, is_delete, loc);
    });

});
