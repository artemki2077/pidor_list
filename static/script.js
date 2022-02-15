function update()
	{$.getJSON('https://script.google.com/macros/s/AKfycbxim1y5h9u-SitfTC9JwlKDb3NOlRgmu3ZYczUWRc_JrT_H9DhLQeC3Hi9cFsLsCxsB9Q/exec?f=board', 
		function(data) {
			document.getElementById("leadeboard").innerHTML="";
			var n = 1;
			data.people.sort((a, b) => {
				if (a.points == b.points){
					if (a.who.lenght > b.who.lenght){
						return 1
					}else if(a.who.lenght == b.who.lenght){
						return 0
					}else{
						return -1
					}
				}else if(a.points > b.points){
					return -1
				}else{
					return 1
				}
			})
			
			data.people.forEach(function name(i, index, arr) {
				document.getElementById("leadeboard").innerHTML += `<h2 class="name"><a class="link" href="/data/${i.who}">${n}. ${i.who} </a><span class="points">${i.points}</span></h2>`;
				n += 1;
			})
	});}


update();
setInterval(
  update,
  3000
);