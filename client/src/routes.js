import HelloWorld from "./components/HelloWorld.vue";
import Soap from "./components/Soap.vue";

const routes = [
    { path: "/", component: HelloWorld },
    { path: "/soap", component: Soap }
];

export default routes;