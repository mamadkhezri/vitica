import { WalletConnectProvider } from "@walletconnect/web3-provider";

document.addEventListener('DOMContentLoaded', () => {
  const connectWalletButton = document.getElementById('connectWalletButton');
  
  connectWalletButton.addEventListener('click', async () => {
    try {
      // Initialize WalletConnect
      const provider = new WalletConnectProvider({
        infuraId: 'YOUR_INFURA_PROJECT_ID', // Replace with your Infura Project ID
      });

      // Enable the provider
      await provider.enable();

      // Access the user's account
      const accounts = await provider.request({ method: 'eth_accounts' });
      console.log('Connected account:', accounts[0]);

      // Use 'provider' for interacting with the blockchain
    } catch (error) {
      console.error(error);
    }
  });
});
