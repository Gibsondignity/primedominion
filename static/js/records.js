$(document).ready(function() {
    // DataTable initialisation
    $('#example').DataTable({
      "paging": true,
      "autoWidth": true,
      "columnDefs": [
        {
          "targets": 3,
          render: function(data, type, full, meta) {
            if (type === 'display' && data == 'Done') {
              var rowIndex = meta.row+1;
              $('#example tbody tr:nth-child('+rowIndex+')').addClass('lightRed');
              return data;
            } else {
              return data;
            }
          }
        }]
    });
  });