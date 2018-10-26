import sys, os
from pymol import cmd
def setdefaults():
    cmd.color('black', 'name C')
    cmd.color('yellow', 'name S')
    cmd.hide('lines', 'all')
    cmd.set('stick_radius',0.1)
    cmd.set('sphere_scale',0.25)
    cmd.set('sphere_scale',1,'name au')
    cmd.set('sphere_scale',1,'name ag')
    cmd.color('grey90', 'name ag')
    cmd.color('gold', 'name au')
    cmd.set('antialias',2)
    cmd.set('opaque_background',0)
    cmd.set('ray_trace_gain',5)
    cmd.set('depth_cue',0)
    cmd.show('sticks','all')
    cmd.show('spheres','all')


from pymol import cgo, CmdException


def cgo_modevec(atom1='pk1', atom2='pk2', radius=0.05, gap=0.0, hlength=-1, hradius=-1,
              color='green', name='',scalefactor=10.0, cutoff=0.6, transparency=1.0): #was 0.6cut 12 scale
## scalefactor was 10.0 
    '''
DESCRIPTION

    Create a CGO mode vector starting at atom1 and pointint in atom2 displacement

ARGUMENTS

    atom1 = string: single atom selection or list of 3 floats {default: pk1}

    atom2 = string: displacement to atom1 for modevec

    radius = float: arrow radius {default: 0.5}

    gap = float: gap between arrow tips and the two atoms {default: 0.0}

    hlength = float: length of head

    hradius = float: radius of head

    color = string: one or two color names {default: blue red}

    name = string: name of CGO object
    
    scalefactor = scale how big of an arrow to make. Default 5

    transparency = 0.0 ~ 1.0, default=1.0 means being totally opaque
    '''
    from chempy import cpv

    radius, gap = float(radius), float(gap)
    hlength, hradius = float(hlength), float(hradius)
    scalefactor, cutoff = float(scalefactor), float(cutoff)
    transparency = float(transparency)
    try:
        color1, color2 = color.split()
    except:
        color1 = color2 = color
    color1 = list(cmd.get_color_tuple(color1))
    color2 = list(cmd.get_color_tuple(color2))

    def get_coord(v):
        if not isinstance(v, str):
            return v
        if v.startswith('['):
            return cmd.safe_list_eval(v)
        return cmd.get_atom_coords(v)

    xyz1 = get_coord(atom1)
    xyz2 = get_coord(atom2)
    newxyz2 = cpv.scale(xyz2, scalefactor)
    newxyz2 = cpv.add(newxyz2, xyz1)
    xyz2 = newxyz2
#    xyz2 = xyz2[0]*scalefactor, xyz2[1]*scalefactor, xyz2[2]*scalefactor
    normal = cpv.normalize(cpv.sub(xyz1, xyz2))

    if hlength < 0:
        hlength = radius * 3.0
    if hradius < 0:
        hradius = hlength * 0.6

    if gap:
        diff = cpv.scale(normal, gap)
        xyz1 = cpv.sub(xyz1, diff)
        xyz2 = cpv.add(xyz2, diff)

    xyz3 = cpv.add(cpv.scale(normal, hlength), xyz2)

# dont draw arrow if distance is too small
    distance = cpv.distance(xyz1, xyz2)
    if distance <= cutoff:
        return

#### generate transparent arrows; 
#### The original codes are the next block
####  --Ran
    obj = [25.0, transparency, 9.0] + xyz1 + xyz3 + [radius] + color1 + color2 + \
          [25.0, transparency, 27.0] + xyz3 + xyz2 + [hradius, 0.0] + color2 + color2 + \
          [1.0, 0.0]

#    obj = [cgo.CYLINDER] + xyz1 + xyz3 + [radius] + color1 + color2 + \
#          [cgo.CONE] + xyz3 + xyz2 + [hradius, 0.0] + color2 + color2 + \
#          [1.0, 0.0]

    if not name:
        name = cmd.get_unused_name('arrow')

    cmd.load_cgo(obj, name)



for i in os.listdir(sys.argv[2]):
    (name,ext) = os.path.splitext(i)
    if ext != '.pymol':
        continue
    cmd.load(sys.argv[1])
    execfile(sys.argv[2]+'/'+i)
    print(name)
    print(ext)

    print('loaded ' + str(sys.argv[1]))
    setdefaults()
    #get string for set_view by launching pymol, loading your molecule, orienting your camera, and typing get_view
    #trans molecule settings
    cmd.set_view('0.924277782, 0.381540447, -0.011579392,\
     -0.381691813,    0.923449934,   -0.039377864,\
     -0.004331028,    0.040815823,    0.999157548,\
     0.000000000,    0.000000000,  -51.879997253,\
     -0.274325967,    0.714184761,    0.048670888,\
     41.411201477,   62.348793030,  -20.000000000' )


#    cmd.set_view ('-0.489665985,    0.810235858,   -0.322092235,\
#     -0.726767302,   -0.175198212,    0.664162636,\
#     0.481701165,    0.559303701,    0.674641192,\
#     0.000000900,   -0.000002144,  -37.252788544,\
#     0.406180322,    0.234906569,    0.471133351,\
#     29.920915604,   44.584514618,  -20.000000000' )


    print('setting default values for ray tracing')
    cmd.png(sys.argv[2]+'/'+name+'.png', dpi=300, width=2400, height=1800, ray=1)
    cmd.delete('all')