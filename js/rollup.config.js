import nodeResolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import babel from '@rollup/plugin-babel';
import replace from '@rollup/plugin-replace';
import terser from '@rollup/plugin-terser';

// https://www.codeguage.com/blog/setup-rollup-for-react

export default {
   input: 'src/index.js',
   output: [
      {
         file: "../reactpy_github_buttons/bundle.js",
         format: "esm",
      },
		{
			file: '../reactpy_github_buttons/bundle.min.js',
			format: 'esm',
			plugins: [terser()]
		}
   ],

   // https://www.mixmax.com/engineering/rollup-externals

   // external: ['react', 'react-dom'],
   // globals: {
   //   'react': 'React',
   //   'react-dom': 'ReactDOM'
   // },

   plugins: [
      nodeResolve({
         extensions: ['.js', '.jsx']
      }),
      babel({
         babelHelpers: 'bundled',
         presets: ['@babel/preset-react'],
         extensions: ['.js', '.jsx']
      }),
      commonjs(),
      replace({
         preventAssignment: false,
         'process.env.NODE_ENV': '"development"'
      })
   ]
}