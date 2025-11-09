module.exports = function (api) {
    api.cache(true);
    return {
      presets: [
        "babel-preset-expo",
        // Temporarily disabled NativeWind to fix Reanimated error
        // ["babel-preset-expo", { jsxImportSource: "nativewind" }],
        // "nativewind/babel",
      ],
      plugins: [
        // Temporarily disabled Reanimated plugin to fix React 19 compatibility issue
        // React Navigation might not work perfectly without it, but let's try
        // "react-native-reanimated/plugin",
      ],
    };
  };