from ovito import *
from ovito.io import *
from ovito.modifiers import *
from ovito.data import NearestNeighborFinder
import numpy as np

# Import a sequence of files.
pipeline = import_file('../dump.water.3', multiple_frames = True)
pipeline.modifiers.append(SelectTypeModifier(property = 'Particle Type', types = {2}))
modifier = IdentifyDiamondModifier()
modifier.only_selected = True
pipeline.modifiers.append(modifier)


# Loop over all frames of the sequence.
for frame_index in range(pipeline.source.num_frames):    
    #dataset.anim.current_frame = frame_index
    data = pipeline.compute(frame_index)
    num_neighbors=2
    neigh_finder = NearestNeighborFinder(num_neighbors, data)
    mu = np.zeros(3)
    for i in range(data.particles.count):
       if (data.particles.particle_types[i]==2):
            #muparticle=np.zeros(3)
            for neigh in neigh_finder.find(i):
                #print(neigh.delta)
                mu += neigh.delta
                #muparticle += neigh.delta
            #print(muparticle,np.linalg.norm(muparticle))
    mu /= data.particles.count
    munorm = np.linalg.norm(mu)
    structure_property = data.particle_properties.structure_type.array
    numHex=np.count_nonzero(structure_property == IdentifyDiamondModifier.Type.HEX_DIAMOND)
    numCub=np.count_nonzero(structure_property == IdentifyDiamondModifier.Type.CUBIC_DIAMOND)
    print(data.attributes['SourceFrame'],numHex,numCub,mu[0]/munorm,mu[1]/munorm,mu[2]/munorm,munorm)

