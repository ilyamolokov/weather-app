let date = new Date();

(function updateAll() {
  dayOfTheWeekFunc();
  monthFunc();
  timeFunc();
}());
function dayOfTheWeekFunc() {
  let weekday = new Array(7);
  weekday[0] = "Воскресенье";
  weekday[1] = "Понедельник";
  weekday[2] = "Вторник";
  weekday[3] = "Среда";
  weekday[4] = "Четверг";
  weekday[5] = "Пятница";
  weekday[6] = "Суббота";
  let day = weekday[date.getDay()];
  document.getElementById("demo").innerHTML = day;
};

function monthFunc() {
  let month_array = ["Января","Февраля","Марта","Апреля","Мая","Июня","Июля","Августа","Сентября","Октября","Ноября","Декабря",];
  let month=month_array[date.getMonth()];
  let number=date.getDate();
  let year = date.getFullYear();
  document.getElementById("datetime").innerHTML = number+" "+month;
  document.getElementById("year").innerHTML = year;
};

function timeFunc() {
  let hours = date.getHours();
  if (hours < 10) {
    hours = "0"+hours;
  };
  let minutes = date.getMinutes();
  if (minutes < 10) {
    minutes = "0"+minutes;
  };
  document.getElementById("time").innerHTML = hours+":"+minutes;
};
