import json

class ImageGenerator:
    def __init__(self, symbols, path):
        self.filename = path
        self.symbols = json.loads(symbols)


    def generate(self):
        self.generate_js()
        self.generate_html()


    def generate_js(self):
        path = self.filename + ".js"
        andares = f"let andares = {self.symbols['imovel']['symbols']['n_andares']};\n"
        blocos = f"let blocos = {self.symbols['imovel']['symbols']['n_blocos']};\n"
        content = """function setup() {
     width = windowWidth;
     height = windowHeight;
     canvas = createCanvas(width, height);
     canvas.position(0, 0);
     canvas.style('z-index', '-1');
}

function draw() {
    let y = 100;
    let dy = 30;
    let larguraBloco = 500;
    let alturaBloco = 500;
    for(let i = 0; i < andares; i++){
        let x = 100;
        for(let j = 0; j < blocos; j++){
            let x_ = x;
            // desenha
            rect(x, y, larguraBloco, alturaBloco);
            x += larguraBloco;
        }
        y += alturaBloco + dy;
    }
}\n"""
        content = f"{andares}{blocos}{content}"
        with open(path, "w") as f:
            f.write(content)


    def generate_html(self):
        path = "index.html"
        content = """<!DOCTYPE html>
<html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/p5.min.js"> </script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/addons/p5.dom.min.js"> </script>
        <script src="{}.js"> </script>
    </head>
    <body>
    </body>
</html>""".format(self.filename)
        with open(path, "w") as f:
            f.write(content)

