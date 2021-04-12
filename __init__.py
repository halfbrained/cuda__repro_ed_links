from cudatext import *

"""
in the Editor of created dialog: links are unclickable 
"""

class Command:
        
    def run(self):
        h, editor = self.init_form()
        
        # both dont work
        #dlg_proc(h, DLG_SHOW_NONMODAL)
        dlg_proc(h, DLG_SHOW_MODAL)
        
    def init_form(self):
        h = dlg_proc(0, DLG_CREATE)

        dlg_proc(h, DLG_PROP_SET, prop={
                'w': 200,
                'h': 100,
                })

        n = dlg_proc(h, DLG_CTL_ADD, 'editor')
        dlg_proc(h, DLG_CTL_PROP_SET, index=n, prop={
                'align': ALIGN_CLIENT,
                })
        h_ed = dlg_proc(h, DLG_CTL_HANDLE, index=n)
        ed = Editor(h_ed)

        ed.set_text_all('\nhttp://t.co\n')

        return h, ed
        