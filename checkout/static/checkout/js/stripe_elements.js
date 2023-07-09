/*
    Core logic/payment from Stripe:
    https://stripe.com/docs/payments/accept-card-payments?platform=web&ui=elements

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/


var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
    },
    invalid: {
        color: '#dc3545', // color matches bootstrap danger class
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {
    style: style
});
card.mount('#card-element');