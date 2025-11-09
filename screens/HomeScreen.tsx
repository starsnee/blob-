import { useEffect } from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { API_BASE_URL } from '../config';

export default function HomeScreen() {
  useEffect(() => {
    const fetchPing = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/api/ping`);
        const data = await response.text();
        console.log('Ping response:', data);
      } catch (error) {
        console.error('Error fetching ping:', error);
      }
    };

    fetchPing();
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

