$(function () {
    $(window).scroll(function () {
        $(".fadein").each(function () {
            var targetElement = $(this).offset().top;
            var scroll = $(window).scrollTop();
            var windowHeight = $(window).height();
            if (scroll > targetElement - windowHeight + 200) {
                $(this).css("opacity", "1");
                $(this).css("transform", "translateY(0)");
            }
        });
    });
});

$(function () {
    $('form').on('change', 'input[type="file"]', function (e) {
        let file = e.target.files[0],
            reader = new FileReader(),
            $preview = $(".preview");

        if (file.type.indexOf("image") < 0) {
            return false;
        }

        reader.onload = (function (file) {
            return function (e) {
                $preview.empty();
                $preview.append($('<img>').attr({
                    src: e.target.result,
                    width: "150px",
                    class: "preview",
                    title: file.name
                }));
            };
        })(file);

        reader.readAsDataURL(file);
    });
});