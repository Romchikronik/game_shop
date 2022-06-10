$(document).ready(function () {
  $(".item-input").on("input", function () {
    this.value = this.value.replace(this.value, 0);
  });

  $(".addtocart").on("click", function () {
    var button = $(this);
    var delete_button = button.prev().prev();
    var cardPrice = delete_button.parent().prev();
    // var card = cardPrice.prev().prev().parent();
    var input_value = button.prev().val();
    var input = button.prev();
    var cart = $(".cart_add");
    var cartTotal = cart.attr("data-totalitems");
    var task = $("#sum");
    var taskPrice = task.attr("price-total");
    var productPrice = cardPrice.attr("product-price");
    var newCartTotal = parseInt(cartTotal) + 1;
    var newInputValue = parseInt(input_value) + 1;
    if (parseInt(taskPrice) < parseInt(productPrice)) {
      var newTaskPrice = parseInt(taskPrice);
    } else {
      var newTaskPrice = parseInt(taskPrice) - parseInt(productPrice);
    }
    console.log(newTaskPrice);

    button.addClass("sendtocart");
    setTimeout(function () {
      if (parseInt(taskPrice) < parseInt(productPrice)) {
        button.addClass("disabled");
        alert("У вас недостаточно средств");
      } else {
        if (newInputValue > 0) {
          delete_button.removeClass("disabled");
        }
        input.on("input", function () {
          this.value = this.value.replace(this.value, newInputValue);
        });
        button.removeClass("sendtocart");
        input.val(newInputValue);
        task.attr("price-total", newTaskPrice).html(newTaskPrice + " сум");
        cart.addClass("shake").attr("data-totalitems", newCartTotal);
        setTimeout(function () {
          cart.removeClass("shake");
        }, 300);
      }
    });
  });

  var taskStartPrice = $("#sum").attr("price-total");
  $(".delete_from_cart").on("click", function () {
    var button = $(this);
    var button_add = $(".addtocart");
    var input_value = button.next().val();
    var input = button.next();
    var cart = $(".cart_add");
    var cartTotal = cart.attr("data-totalitems");
    var cardPrice = button.parent().prev();
    var task = $("#sum");
    var taskPrice = task.attr("price-total");
    var productPrice = cardPrice.attr("product-price");
    var delCartTotal = parseInt(cartTotal) - 1;
    var newInputValue = parseInt(input_value) - 1;
    var newTaskPrice = parseInt(taskPrice) + parseInt(productPrice);
    console.log(newTaskPrice);

    button.addClass("sendtocart");

    setTimeout(function () {
      if (
        parseInt(taskPrice) === parseInt(taskStartPrice) ||
        newInputValue < 0
      ) {
        button.addClass("disabled");
        alert("Вы все продали, куда еще?");
      } else {
        input.on("input", function () {
          this.value = this.value.replace(this.value, newInputValue);
        });
        input.val(newInputValue);
        task.attr("price-total", newTaskPrice).html(newTaskPrice + " сум");
        button.removeClass("sendtocart");
        button_add.removeClass("disabled");
        cart.attr("data-totalitems", delCartTotal);
      }
    });
  });

  var onOff = true;
  var onOff2 = true;

  // кнопка навигации на сайте
  $(".nav__burger").click(function () {
    if (!$(this).hasClass("open")) {
      $(this).addClass("open");
      $("html").css("overflow-y", "hidden");
      $(".nav-menu").addClass("menu-open");
      $(".nav").addClass("fixed-top");
      onOff2 = false;
    } else {
      $(this).removeClass("open");
      $(".nav-menu").removeClass("menu-open");
      $("html").css("overflow", "auto");
      if (onOff == true) {
        $(".nav").removeClass("fixed-top");
      }
      onOff2 = true;
    }
  });

  $(function () {
    setTimeout(function () {
      $(".fill-limit").each(function () {
        var me = $(this);
        var perc = me.attr("data-limit");
        var current_perc = 0;

        if (!$(this).hasClass("stop")) {
          var progress = setInterval(function () {
            if (current_perc >= perc) {
              clearInterval(progress);
            } else {
              current_perc += 1;
              me.parent()
                .children()
                .children(".filler")
                .css("height", current_perc + "%");
              me.html(current_perc + "<span>%</span>");
            }
          }, 6);

          me.addClass("stop");
          me.parent().children().children(".filler").addClass("stop");
        }
      });
    }, 0);
  });

  // Язык
  $(".nav-menu__lang").click(function (e) {
    e.preventDefault();
    if ($(".lang__uzb").hasClass("close_link")) {
      $(".lang__uzb").removeClass("close_link");
      $(".lang__ru").addClass("close_link");
    } else {
      $(".lang__ru").removeClass("close_link");
      $(".lang__uzb").addClass("close_link");
    }
  });

  // Фильтр
  $(".dropdown__toggle").click(function () {
    $(".dropdown__menu").slideToggle(150);
  });

  // Получить задание
  $(".get_task").click(function (e) {
    e.preventDefault();
    $(".overlay").show().css("overflow", "auto");
    $("html").css("overflow-y", "hidden");
    $("#task").animate({
      top: "50%",
    });
  });
  // Выплывающее окно
  $(".task-block__close, .overlay").click(function () {
    $(".overlay").hide();
    $("html").css("overflow-y", "scroll");
    $("#task").animate({
      top: "-100%",
    });
  });
  // Выплывающее окно
  $(".get_instruction").click(function (e) {
    e.preventDefault();
    $(".overlay").show().css("overflow", "auto");
    $("html").css("overflow-y", "hidden");
    $("#instruction").animate({
      top: "50%",
    });
  });

  $(".task-block__close, .overlay").click(function () {
    $(".overlay").hide();
    $("html").css("overflow-y", "scroll");
    $("#instruction").animate({
      top: "-100%",
    });
  });

  // График
  $(".btn-order").click(function (e) {
    e.preventDefault();
    $(".ui-264").css("display", "block");
  });
});
