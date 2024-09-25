#!/usr/bin/yarn dev
import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

process.on('SIGINT', () => {
  client.quit(() => {
    console.log('Redis client disconnected');
    process.exit(0);
  });
});
