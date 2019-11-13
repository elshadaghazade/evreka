$(document).ready(function(){
    let clicked_vehicle_info = {}

    $('.input-group.date').datepicker({});

    $('#route-table thead th').each( function () {
        let title = $(this).text();
        $(this).append(`<input type="text" placeholder="Search ${title}">`);
    } );

    var table = $('#route-table').DataTable({
        bPaginate: false,
        bFilter: true
    });

    table.columns().every( function () {
        var that = this;
    
        $('input', this.header()).on('keyup change clear', function () {
            that.search(this.value).draw();
        });
    });


    // vehicle on click
    // data-toggle="tooltip" data-placement="top" title="Click to change"
    $('#route-table tbody tr').each(function(){
        let that = this;
        let td = $(this).find('td:eq(1)')
        td.attr({'title': 'Click to change'});
        td.addClass('vehicle-td')
        td.on('click', function(e){
            let x = e.clientX;
            let y = e.clientY;

            $('.change-menu').css({
                left: x,
                top: y
            }).show();

            clicked_vehicle_info = {}
            $(that).find('td').each(function(index){
                let title = $('#route-table thead th').eq(index).text()
                clicked_vehicle_info[title] = $(this).text();
            });
        });
    });

    $(window).on('keyup', function(e){
        if (e.key === 'Escape') {
            $('.change-menu').hide();
        }
    });

    $('.change-menu').on('click', function(){
        $(this).hide();
    });

    $('#changeModal').on('show.bs.modal', function(){
        $('.modal-title').html(`${clicked_vehicle_info.Vehicle} - ${clicked_vehicle_info.Name} - ${clicked_vehicle_info.Driver}`)
    })
});