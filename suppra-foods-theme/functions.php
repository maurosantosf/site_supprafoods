<?php
/**
 * Suppra Foods Theme Functions
 */

defined('ABSPATH') || exit;

// Enqueue styles and scripts
add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style('suppra-landing-css', get_template_directory_uri() . '/assets/css/landing-page.css', [], '1.0.0');
    wp_enqueue_script('suppra-landing-js', get_template_directory_uri() . '/assets/js/landing-page.js', [], '1.0.0', true);
});

// Remove admin bar on front-end for cleaner look
add_filter('show_admin_bar', '__return_false');

// Add theme support
add_action('after_setup_theme', function() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', ['search-form', 'comment-form', 'comment-list', 'gallery', 'caption']);
});
