// Temporarily simplified to avoid Reanimated error
// Will add navigation back once Reanimated compatibility is fixed
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { useEffect, useState } from 'react';
import { API_BASE_URL } from './config';

export default function App() {
  const [connectionStatus, setConnectionStatus] = useState<'checking' | 'connected' | 'disconnected'>('checking');
  const [errorMessage, setErrorMessage] = useState<string>('');

  useEffect(() => {
    // Delay fetch slightly to ensure component is fully mounted
    const timeoutId = setTimeout(() => {
      const fetchPing = async () => {
        try {
          const url = `${API_BASE_URL}/api/ping`;
          console.log('Fetching from:', url);
          
          const response = await fetch(url, {
            method: 'GET',
            headers: {
              'Accept': 'text/plain',
              'ngrok-skip-browser-warning': 'true',
            },
          });
          
          if (!response.ok) {
            const errorText = await response.text();
            console.error('Ping failed with status:', response.status, response.statusText);
            console.error('Error response:', errorText);
            setConnectionStatus('disconnected');
            setErrorMessage(errorText || `HTTP ${response.status}`);
            return;
          }
          
          const data = await response.text();
          console.log('Ping response:', data);
          
          if (data.trim() === 'pong') {
            console.log('✅ Successfully received pong from backend!');
            setConnectionStatus('connected');
            setErrorMessage('');
          } else {
            console.warn('Unexpected response:', data);
            setConnectionStatus('disconnected');
            setErrorMessage(`Unexpected response: ${data}`);
          }
        } catch (error) {
          console.error('Error fetching ping:', error);
          setConnectionStatus('disconnected');
          if (error instanceof Error) {
            console.error('Error message:', error.message);
            setErrorMessage(error.message);
          } else {
            setErrorMessage('Unknown error occurred');
          }
        }
      };

      fetchPing();
    }, 100);

    return () => clearTimeout(timeoutId);
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Blob App</Text>
      
      <View style={styles.statusContainer}>
        <View style={[styles.statusIndicator, connectionStatus === 'checking' && styles.statusChecking, connectionStatus === 'connected' && styles.statusConnected, connectionStatus === 'disconnected' && styles.statusDisconnected]} />
        <Text style={styles.statusText}>
          {connectionStatus === 'checking' && 'Checking connection...'}
          {connectionStatus === 'connected' && '✅ Backend Connected'}
          {connectionStatus === 'disconnected' && '❌ Backend Offline'}
        </Text>
      </View>

      {connectionStatus === 'disconnected' && (
        <View style={styles.errorContainer}>
          <Text style={styles.errorTitle}>Backend not available</Text>
          <Text style={styles.errorMessage}>{errorMessage}</Text>
          <Text style={styles.errorHint}>
            Make sure your backend server is running and ngrok is active.
          </Text>
          <Text style={styles.errorHint}>
            Update the URL in config.ts if your ngrok URL has changed.
          </Text>
        </View>
      )}

      {connectionStatus === 'connected' && (
        <Text style={styles.successMessage}>
          Successfully connected to backend! 🎉
        </Text>
      )}

      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  text: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 30,
  },
  statusContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 20,
  },
  statusIndicator: {
    width: 12,
    height: 12,
    borderRadius: 6,
    marginRight: 8,
  },
  statusChecking: {
    backgroundColor: '#FFA500',
  },
  statusConnected: {
    backgroundColor: '#4CAF50',
  },
  statusDisconnected: {
    backgroundColor: '#F44336',
  },
  statusText: {
    fontSize: 18,
    fontWeight: '600',
  },
  errorContainer: {
    backgroundColor: '#FFEBEE',
    padding: 15,
    borderRadius: 8,
    marginTop: 20,
    maxWidth: '90%',
  },
  errorTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#C62828',
    marginBottom: 8,
  },
  errorMessage: {
    fontSize: 14,
    color: '#D32F2F',
    marginBottom: 12,
  },
  errorHint: {
    fontSize: 12,
    color: '#666',
    marginTop: 4,
    textAlign: 'center',
  },
  successMessage: {
    fontSize: 16,
    color: '#4CAF50',
    marginTop: 20,
    fontWeight: '600',
    textAlign: 'center',
  },
});
