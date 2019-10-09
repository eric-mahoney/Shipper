loadbackgrounds = () => {
  console.log("about to select a background");
  const backgrounds = [
    ["linear-gradient(45deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%)", "#000"],
    ["linear-gradient(to top, #a18cd1 0%, #fbc2eb 100%)", "#000"],
    ["linear-gradient(to top, #fad0c4 0%, #ffd1ff 100%)", "#000"],
    ["linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%)", "#000"],
    ["linear-gradient(120deg, #e0c3fc 0%, #8ec5fc 100%)", "#000"],
    ["linear-gradient(to top, #feada6 0%, #f5efef 100%)", "#000"],
    ["linear-gradient(to top, #a3bded 0%, #6991c7 100%)", "#000"],
    ["linear-gradient(-225deg, #7DE2FC 0%, #B9B6E5 100%)", "#000"],
    ["linear-gradient(-225deg, #FFE29F 0%, #FFA99F 48%, #FF719A 100%)", "#000"],
    ["linear-gradient(-225deg, #A8BFFF 0%, #884D80 100%)", "#000"],
    ["linear-gradient(to top, #df89b5 0%, #bfd9fe 100%)", "#000"],
    ["linear-gradient(to right, #ed6ea0 0%, #ec8c69 100%)", "#000"],
    ["linear-gradient(-45deg, #FFC796 0%, #FF6B95 100%)", "#000"],
    ["linear-gradient(to right, #243949 0%, #517fa4 100%)", "#fff"],
    ["linear-gradient(to top, #1e3c72 0%, #1e3c72 1%, #2a5298 100%)", "#fff"],
    ["linear-gradient(45deg, #ee9ca7 0%, #ffdde1 100%)", "#000"],
    ["linear-gradient(-20deg, #f794a4 0%, #fdd6bd 100%)", "#000"],
    ["linear-gradient(to top, #4481eb 0%, #04befe 100%)", "#000"],
    ["linear-gradient(-20deg, #2b5876 0%, #4e4376 100%)", "#fff"]
  ];
  random_int = Math.floor(Math.random() * backgrounds.length);
  console.log("the random integer is: " + String(random_int));
  background_color = backgrounds[random_int][0];
  font_color = backgrounds[random_int][1];
  console.log("changing background color to " + background_color);
  console.log("changing font color to: " + font_color);

  document.body.style.backgroundImage = background_color;
  document.body.style.color = font_color;
  if (document.querySelector(".table")) {
    document.querySelector(".table").style.color = font_color;
  }
};

window.onload = function() {
  loadbackgrounds();
};
