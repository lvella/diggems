var ctx;

function idx(m, n) {
    return params.mine[m*16 + n]
}

/*
function init_map() {
    // Create map object
    map = new Array(16);
    for(var i = 0; i < 16; ++i) {
	map[i] = new Array(16);
	for(var j = 0; j < 16; ++j) {
	    map[i][j] = {'gem': false, 'visible': false};
	}
    }

    // Fill random gems
    for(var i = 0; i < 51; ++i) {
	var m, n;
	do {
	    m = Math.floor(Math.random() * 16);
	    n = Math.floor(Math.random() * 16);
	} while (map[m][n].gem);

	map[m][n].gem = true;
    }
}

function for_each_neighbor(m, n, func) {
    const DIFS = [[-1,-1],[-1,0],[-1,+1],[0,-1],[0,+1],[+1,-1],[+1,0],[+1,+1]];

    for(var i = 0; i < 8; ++i) {
	var a = DIFS[i];
	var x = m + a[0];
	var y = n + a[1];
	if(x >= 0 && x <= 15 && y >= 0 && y <= 15)
	    func(x, y);
    }
}
*/

function draw_square(m, n) {
    const TEXT_COLOR = [
	'rgb(0,0,255)',
	'rgb(0,160,0)',
	'rgb(255,0,0)',
	'rgb(0,0,127)',
	'rgb(160,0,0)',
	'rgb(0,255,255)',
	'rgb(160,,160)',
	'rgb(0,0,0)'
    ];
    var x0 = m * 26;
    var y0 = n * 26;
    function draw() { ctx.fillRect(x0,y0,25,25); }

    tile = idx(m, n)
    if((tile >= 0 && tile <= 8) || tile == 'r' || tile == 'b') {
	ctx.fillStyle = 'rgb(255,216,161)';
	draw();
	if(tile == 'r' || tile == 'b') {
	    ctx.fillStyle = (tile == 'b') ? 'rgb(50,50,200)' : 'rgb(200,50,50)';
	    ctx.beginPath();
	    ctx.arc(x0+12.5, y0+12.5, 5, 0, Math.PI*2, true);
	    ctx.closePath();
	    ctx.fill();
	}
	else if(tile > 0) {
	    ctx.fillStyle = TEXT_COLOR[tile];
	    ctx.fillText(tile, x0 + 12.5, y0 + 12.5);
	}
    }
    else {
	ctx.fillStyle = 'rgb(227,133,0)';
	draw();
    }
}

function on_click(ev) {
    /*
    if(ev.button != 0)
	return;

    var m;
    var n;

    m = ev.clientX + document.body.scrollLeft +
	document.documentElement.scrollLeft - this.offsetLeft;
    n = ev.clientY + document.body.scrollTop +
        document.documentElement.scrollTop - this.offsetTop;

    m = Math.floor(m / 26);
    n = Math.floor(n / 26);

    function reveal(m, n) {
	if(map[m][n].visible)
	    return;

	map[m][n].visible = true;
	var count = draw_square(m, n);
	if(count === 0)
	    for_each_neighbor(m, n, reveal);
    }

    reveal(m, n);
    */
}

function init() {
    var elem = document.getElementById('game_canvas');
    if (!elem || !elem.getContext) {
	// Panic return
	// TODO: add friendly message explaining why IE sucks
	return;
    }
    elem.addEventListener('click', on_click, false);
    ctx = elem.getContext('2d');
    ctx.font = "17pt Helvetica";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";

    if(!params.mine) {
	params.mine = '';
	for(var i = 0; i < 256; ++i)
	    params.mine += '?';
    }

    // Draw map
    for(var i = 0; i < 16; ++i)
	for(var j = 0; j < 16; ++j)
	    draw_square(i, j);
}

window.addEventListener('load', init, false);