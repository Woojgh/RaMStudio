'use strict';

$(document).ready(function () {

    $('.project-photo').click(function () {
        $('#project-selected-image').attr('src', '{{ project.photos.first }}');
    });
});