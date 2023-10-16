from IPython.core.display import HTML

def css_styling():
    styles = """<style>
div.warn {    
    background-color: #fcf2f2;
    border-color: #dFb5b4;
    border-top: 0px;
    border-left: 5px solid #dfb5b4;
    padding: 0.5em;
    }

div.task{    
    background-color: #B0E0E6;
    border-color: #B0E0E6;
    border-top: 0px;
    border-left: 5px solid #1E90FF;
    padding: 0.5em;
    }

div.infobox {    
    background-color: #F5F5DC;
    border-color: #F5F5DC;
    border-top: 0px;
    border-left: 5px solid #DAA520;
    padding: 0.5em;
    }

div.interlude {    
    background-color: #E6E6FA;
    border-color: #E6E6FA;
    border-top: 0px;
    border-left: 5px solid #4B0082;
    padding: 0.5em;
    }
    
div.assessment {    
    background-color: #98FB98;
    border-color: #228B22;
    border-left: 5px solid #228B22;
    padding: 0.5em;
    }

div.acse blockquote{

 background-color: white;

}

 </style>
"""
    return HTML(styles)