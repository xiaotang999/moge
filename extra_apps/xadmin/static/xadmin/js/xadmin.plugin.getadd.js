(function($){

  var DetailsPop = function(element){
    this.$element = $(element);
    this.res_uri = this.$element.data('res-uri');
    // this.edit_uri = this.$element.data('edit-uri');
    this.obj_data = null;

    this.$element.on('click', $.proxy(this.click, this));
  };

  DetailsPop.prototype = {
      constructor: DetailsPop,

      click: function(e){
        // var el = this.$element;
        // console.log(el)
        // console.log(e)

        e.stopPropagation();
        e.preventDefault();
        var modal = $('#detail-modal-id');
        var el = this.$element;
        if(!modal.length){
          modal = $('<div id="detail-modal-id" class="modal fade detail-modal" role="dialog"><div class="modal-dialog"><div class="modal-content">'+
            '<div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button><h4 class="modal-title">'+ 
            el.attr('title') +'</h4></div><div class="modal-body"></div>'+
            '<div class="modal-footer"><button class="btn btn-default" data-dismiss="modal" aria-hidden="true">'+gettext('Close')+'</button>'+
            '</div></div></div></div>');
          $('body').append(modal);
        }
        modal.find('.modal-title').html(el.attr('title'));
        var _url = "http://www.ip138.com/ips138.asp?ip="+this.res_uri+"&action=2"
        // var _url = "http://whois.pconline.com.cn/ip.jsp?ip="+this.res_uri

        modal.find('.modal-body').html('<iframe src="'+_url+'" width="100%"  height="400px"></iframe>');

        modal.modal();

      }
  };


  $.fn.GetAdd = function () {
    return this.each(function () {
     
      var $this = $(this), data = $this.data('details');
      if (!data) {
          $this.data('details', (data = new DetailsPop(this)));
          // alert('asd')
      }
    });
  };

  $(function(){
    $('.get-add').GetAdd();
  });


})(jQuery);


