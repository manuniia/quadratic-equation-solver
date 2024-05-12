from quadratic_package_solver_marboi import quadratic
import tkinter as tk


def main():
    window  = tk.Tk()

    tk.Label(window, text='A').grid(row=0) 
    txtA = tk.Entry(window,width=15)
    txtA.grid(column=1, row=0)
    txtA.focus()
    
    tk.Label(window, text='B').grid(row=1) 
    txtB = tk.Entry(window,width=15)
    txtB.grid(column=1, row=1)

    tk.Label(window, text='C').grid(row=2) 
    txtC = tk.Entry(window,width=15)
    txtC.grid(column=1, row=2)
    resultBox = tk.Label()
    resultBox.grid(column=1, row=5)

    def clicked():
        try:
            a = int(txtA.get())
        except:
            resultBox.config(text='value A is not a number, please fix it')
            return
        if a==0:
            resultBox.config(text='')
            return

        try:
            b = int(txtB.get())
        except:
            resultBox.config(text='value B is not a number, please fix it')
            return
        
        try:
            c = int(txtC.get())
        except:
            resultBox.config(text='value C is not a number, please fix it')
            return

        root1, root2 = quadratic.solve_quadratic(a, b, c)

        if (root1 == None):
            resultBox.config(text='The equation has no roots')
            return

        if (root2 == None):
            resultBox.config(text=f'The equation has one root: {root1}')
            return

        resultBox.config(text=f'The equation has two roots: {root1}  and {root2}')

    btn = tk.Button(window, text="Calculate roots", command=clicked) 
    btn.grid(column=1, row=4)

    window.mainloop()


if __name__ == "__main__":
    main()