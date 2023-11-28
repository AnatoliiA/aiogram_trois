#!/usr/bin/env python3
import git

import pdoc

if __name__ == "__main__":
    doc = pdoc.doc.Module(git)

    # We can override most pdoc doc attributes by just assigning to them.
    doc.get("Foo.A").docstring = "I'm a docstring for Foo.A."
    pdoc.render.configure(docformat="google", include_undocumented=True)
    out = pdoc.render.html_module(module=doc, all_modules={"m": doc})
    with open("foo.html", "w") as f:
        f.write(out)