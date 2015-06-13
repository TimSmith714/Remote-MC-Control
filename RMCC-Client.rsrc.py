{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Standard Template with File->Exit menu',
          'size':(643, 288),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'Button', 
    'name':'btnMoveDown', 
    'position':(500, 79), 
    'label':u'Move Down', 
    },

{'type':'Button', 
    'name':'btnMoveUp', 
    'position':(499, 21), 
    'label':u'Move Up', 
    },

{'type':'Button', 
    'name':'btnFlyMode', 
    'position':(500, 49), 
    'label':u'Fly Mode', 
    },

{'type':'Button', 
    'name':'btnLookDown', 
    'position':(401, 52), 
    'label':u'LookDown', 
    },

{'type':'Button', 
    'name':'btnLookUp', 
    'position':(401, 21), 
    'label':u'Look Up', 
    },

{'type':'Button', 
    'name':'strTurnRight', 
    'position':(280, 10), 
    'label':u'Turn Right', 
    },

{'type':'Button', 
    'name':'btnTurnLeft', 
    'position':(35, 11), 
    'label':u'Turn Left', 
    },

{'type':'Button', 
    'name':'btnStrafeRight', 
    'position':(292, 50), 
    'label':u'Strafe Right', 
    },

{'type':'Button', 
    'name':'btnStrafeLeft', 
    'position':(11, 50), 
    'label':u'Strafe Left', 
    },

{'type':'Button', 
    'name':'btnBack', 
    'position':(162, 81), 
    'label':u'Back', 
    },

{'type':'Button', 
    'name':'btnRight', 
    'position':(200, 49), 
    'label':u'Right', 
    },

{'type':'Button', 
    'name':'btnLeft', 
    'position':(102, 49), 
    'label':u'Left', 
    },

{'type':'Button', 
    'name':'btnForward', 
    'position':(160, 11), 
    'label':u'Forward', 
    },

] # end components
} # end background
] # end backgrounds
} }
