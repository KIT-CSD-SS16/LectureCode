#! /usr/bin/env python3.4
import math

PDGDictionary = {
        511 : [5279.6, 'B0'],
        421 : [1864.8, 'D0'],
        113 : [ 775.3, 'Rho0'],
        211 : [ 139.6, 'Pi+'],
        321 : [ 493.7, 'K+'],
      20113 : [1260.0, 'a1'],
         13 : [ 105.7, 'mu+'],
         14 : [   0.0, 'nu']
        }

class Particle:

    def __init__(self, pdgCode, mother):
        self.pdgCode = pdgCode
        self.mass, self.name = PDGDictionary[pdgCode]
        self.mother  = mother

    def getSpeed(self):
        '''
        Calculates the speed of a particle under the assumption of
           * all decays happening as back2back 2-body decays,
           * Newtonian mechanics,
           * all angles stay in the initial single dimension,
           [* all momenta are reflected in the same direction].
        '''
        if not self.mother:
            return 0
        v = self.mother.getSpeed() + self.mother.getDecayMomentum()/self.mass
        return v


class DecayParticle(Particle):

    def __init__(self, pdgCode, mother):
        super().__init__(pdgCode, mother)
        self.daughters = []

    def addDaughter(self, daughter):
        self.daughters.append(daughter)

    def printParticleChainInfo(self):
        print ('Name: ' + self.name + ', Mass: ' + str(self.mass))
        for daughter in self.daughters:
            daughter.printParticleChainInfo()

    def getDecayMomentum(self):
        '''
        Calculates the momentum of the daughters in the rest system of the particel itself.
        '''
        if len(self.daughters) != 2:
            print('Error, this case is\'nt foreseen yet!')
            return None
        Q = self.mass - self.daughters[0].mass - self.daughters[1].mass
        return math.sqrt(Q)


class StableParticle(Particle):

    def __init__(self, pdgCode, mother):
        super().__init__(pdgCode, mother)

    def printParticleChainInfo(self):
        print ('Name: ' + self.name + ', Mass: ' + str(self.mass))

# class ParticleFactory:

class ParticleFactoryCollider:

    DecayChainDictionary = {
        511 : [421, 20113],
        421 : [321, 211],
      20113 : [113, 211],
        113 : [211, 211],
        211 : None,
        321 : None
        }

    def getParticleChain(self, pdgNumber, mother = None):
        subParticleList = self.DecayChainDictionary[pdgNumber]
        if subParticleList:
            particle = DecayParticle(pdgNumber, mother)
            daughter1 = self.getParticleChain(subParticleList[0], particle)
            daughter2 = self.getParticleChain(subParticleList[1], particle)
            particle.addDaughter(daughter1)
            particle.addDaughter(daughter2)
        else:
            particle = StableParticle(pdgNumber, mother)
        return particle


class ParticleFactoryFixedTarget:

    DecayChainDictionary = {
        511 : [421, 20113],
        421 : [321, 211],
      20113 : [113, 211],
        113 : [211, 211],
        211 : [13,   14],
        321 : [13,   14],
         13 : None,
         14 : None
        }

    def getParticleChain(self, pdgNumber, mother = None):
        subParticleList = self.DecayChainDictionary[pdgNumber]
        if subParticleList:
            particle = DecayParticle(pdgNumber, mother)
            daughter1 = self.getParticleChain(subParticleList[0], particle)
            daughter2 = self.getParticleChain(subParticleList[1], particle)
            particle.addDaughter(daughter1)
            particle.addDaughter(daughter2)
        else:
            particle = StableParticle(pdgNumber, mother)
        return particle


def main():

    B0 = DecayParticle(511, None)
    D0 = DecayParticle(421, B0)
    fastPion = StableParticle(211, B0)
    B0.addDaughter(D0)
    B0.addDaughter(fastPion)
    pion = StableParticle(211, D0)
    D0.addDaughter(pion)
    kaon = StableParticle(321, D0)
    D0.addDaughter(kaon)

    D0.printParticleChainInfo()
    print (D0.getSpeed())
    print (pion.getSpeed())

    print ('\nColliderFactory')
    particleFactory = ParticleFactoryCollider()

    B = particleFactory.getParticleChain(511)
    B.printParticleChainInfo()

    print ('\nFixedTargeFactory')
    particleFactory = ParticleFactoryFixedTarget()

    B = particleFactory.getParticleChain(511)
    B.printParticleChainInfo()

if __name__ == "__main__":
    main()
