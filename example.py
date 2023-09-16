from hybrid import interface






if __name__ == '__main__':

    def main(data):
        print(data)

    d1 = interface.title(content='Hybrid with Ant Design UI', level=2)
    d2 = interface.slider(onChange=main)
    image = interface.image(src="https://gw.alipayobjects.com/zos/rmsportal/KDpgvguMpGfqaHPjicRK.svg", alt='hallo', width='350px', height='350px')
    content = interface.content(content=[d1,d2, image])

    app = interface.compiler(layout=content,globale_ui_style='main.css')
    app.run()