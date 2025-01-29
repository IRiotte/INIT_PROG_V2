

/**
 * Class Chat
 */
public class Chat {

		//
		// Fields
		//

  private String nom;
  private int bavard;
  
		//
		// Constructors
		//
		public Chat () { };
  
		//
		// Methods
		//


		//
		// Accessor methods
		//

		/**
		 * Set the value of nom
		 * @param newVar the new value of nom
		 */
  public void setNom (String newVar) {
  		nom = newVar;
  }

		/**
		 * Get the value of nom
		 * @return the value of nom
		 */
  public String getNom () {
  		return nom;
  }

		/**
		 * Set the value of bavard
		 * @param newVar the new value of bavard
		 */
  public void setBavard (int newVar) {
  		bavard = newVar;
  }

		/**
		 * Get the value of bavard
		 * @return the value of bavard
		 */
  public int getBavard () {
  		return bavard;
  }

		//
		// Other methods
		//

		/**
		 * @param        nomDuChat
		 * @param        bavard
		 */
  public void Chat(String nomDuChat, int bavard)
  {
				this.nom = nomDuChat;
				this.bavard = bavard;
		}


		/**
		 * @param        nomDuChat
		 */
  public void Chat(String nomDuChat)
  {
				this(nomDuChat, 1);
		}


		/**
		 * @return       String
		 */
  public String getNom()
  {
				return this.nom;
		}


		/**
		 * @param        nouveauNom
		 */
  public void setNom(String nouveauNom)
  {
				this.nom = nouveauNom;
		}


		/**
		 */
  public void devientMuet()
  {
				this.bavard = 0;
		}


		/**
		 */
  public void miaule()
  {
				System.out.print(this.nom);
				        for (int i = 0; i < this.bavard; ++i) {
				            System.out.print(" Miaou !");
				        }
				        System.out.println(" ...");
		}


		/**
		 * @return       Boolean
		 * @param        heure
		 */
  public Boolean estEndormi(double heure)
  {
				return (heure <= 3 | | heure > 4);
		}


}
