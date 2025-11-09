import { useEffect } from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { API_BASE_URL } from '../config';

export default function HomeScreen() {
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
              'Accept': 'application/json',
              'ngrok-skip-browser-warning': 'true',
            },
          });
          
          if (!response.ok) {
            console.error('Ping failed with status:', response.status, response.statusText);
            const errorText = await response.text();
            console.error('Error response:', errorText);
            return;
          }
          
          const data = await response.json();
          console.log('Ping response:', data);
          
          if (data.message === 'pong') {
            console.log('✅ Successfully received pong from backend!');
          } else {
            console.warn('Unexpected response:', data);
          }
        } catch (error) {
          console.error('Error fetching ping:', error);
          if (error instanceof Error) {
            console.error('Error message:', error.message);
            console.error('Error stack:', error.stack);
          }
        }
      };

      fetchPing();
    }, 100);

    return () => clearTimeout(timeoutId);
  }, []);

  return (
    <View style={styles.container}>
      <Text>Open up App.tsx to start working on your app!</Text>
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
  },
});

