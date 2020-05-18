package canut;

import java.util.Random;
import java.util.Vector;

import negoUPV.UPVAgent;
import negotiator.Bid;

public class AgenteCanut extends UPVAgent {
	
	double S;
	double beta;
	double RU;

	@Override
	public boolean acceptOffer(Bid arg0) {
		// Este agente nunca aceptará una oferta
		return false;
	}

	@Override
	public void initialize() {
		beta = 1;
		RU = 0.0;
		S = 0.99;
		update();
		
		rand = new Random(System.currentTimeMillis()+this.getName().hashCode());
		
	}
	
	private void update() {
		
		// Implementar una estrategia de concesion temporal
		S= 1-(1-RU)*Math.pow(1, (1/beta));
	
	}

	@Override
	public Bid proposeOffer() {
		
		Vector<Bid> myBids = getOffers(0.5,0.7);
		
		Bid selected = myBids.get(rand.nextInt(myBids.size()));

		return selected;
	}

	
}
